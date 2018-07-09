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
   values
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
      showDataForYear: ({ dataForSelectedYear }) => (allYearsData, year) => {
        return ({
          monthsForSelectedYear: keys(propOr('', year, allYearsData)[0]),
          expensesForSelectedYear: values(propOr('', year, allYearsData)[0])
        })
      }
   }
 )
)

 export default enhance(ByMonths)
