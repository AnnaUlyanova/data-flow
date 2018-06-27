import {
   compose,
   lifecycle,
 } from 'recompose'

 import {
   keys
 } from 'ramda'

 import { annualExpeneseByMonths } from '../main-data'
 import ByMonths from '../components/ByMonths'

 export const enhance = compose(
   lifecycle({
     componentDidMount(){
         annualExpeneseByMonths.then((monthlyExpenses) => {
           const years = keys(monthlyExpenses)
              this.setState({
                monthlyExpenses: years
              })
         })
     }
   })
 )

 export default enhance(ByMonths)
