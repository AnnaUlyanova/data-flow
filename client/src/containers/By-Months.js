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
        const first = map(objOf('x'), monthsForSelectedYear)
        const second = map(objOf('y'), expensesForSelectedYear)
        const mergeResult2 = []
        for (let i=0; i<first.length; i++) {
          mergeResult2.push(merge(first[i], second[i]))
          i++
        }
        return ({
          monthsForSelectedYear: keys(propOr('', year, allYearsData)[0]),
          expensesForSelectedYear: values(propOr('', year, allYearsData)[0]),
          dataForD3: [{ values: mergeResult2}]
        })
      }
   }
 )
)

 export default enhance(ByMonths)
