import {
   compose,
   lifecycle,
   withStateHandlers,
 } from 'recompose'

 import {
   keys,
   map,
   replace,
   propOr,
   values,
   zipObj,
   objOf,
   merge
 } from 'ramda'

 import { annualExpeneseByMonths, getYears } from '../main-data'
 import ByMonths from '../components/ByMonths'

 export const enhance = compose(
  lifecycle({
    componentDidMount(){
      getYears.then((years) => {
        this.setState({
          years: years
        })
      })
      annualExpeneseByMonths.then((allYearsData) => {
        this.setState({
          allYearsData: allYearsData
        })
      })
     }
  }),
  withStateHandlers(
    ({ initialData = [] }) => ({
      dataForSelectedYear: initialData
    }),
    {
      showDataForYear: ({ dataForSelectedYear }) => (allYearsData, year, monthsForSelectedYear, expensesForSelectedYear) => {
        const generateDataForD3 = (year) => {
          console.log('1111 year', year)
          const months = keys(propOr('', year, allYearsData)[0])
          const expenses = map(parseInt, map(replace('$', ''), values(propOr('', year, allYearsData)[0])))
          const result = []
          for (let i = 0; i < months.length; i++) {
            const dataToPush = {x: months[i], y: expenses[i]}
            result.push(dataToPush)
         }
          return result
        }

        const dataForD3 = [{
          label: year,
          values: generateDataForD3(year)
        }]

        return ({
          monthsForSelectedYear: keys(propOr('', year, allYearsData)[0]),
          expensesForSelectedYear: map(parseInt, values(propOr('', year, allYearsData)[0])),
          dataForD3: dataForD3
        })
      }
   }
 )
)

 export default enhance(ByMonths)
