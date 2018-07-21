import {
   compose,
   lifecycle,
   withStateHandlers,
 } from 'recompose'

 import {
   keys,
   map,
   propOr,
   find,
   prop,
   pathOr,
   flatten,
   values
 } from 'ramda'

 import { expensesByCategories, getYears } from '../main-data'
 import ByCategory from '../components/ByCategory'

 const getCategories = expensesByCategories.then((data) => keys(data))

 export const enhance = compose(
   lifecycle({
     componentDidMount(){
       getCategories.then((categories) => {
         this.setState({
           categories: categories
         })
       })
       expensesByCategories.then((allCategoriesData) => {
         this.setState({
           allCategoriesData: allCategoriesData
         })
       })
      }
   }),
   withStateHandlers(
     ({ initialData = [] }) => ({
       dataForSelectedCategory: initialData
     }),
      { showDataForCategory: ({ dataForSelectedCategory }) => (allCategoriesData, category, toggledData) => {

        const generateDataForD3 = (category, value) => {
          const years = flatten(map(keys, pathOr('', [category], allCategoriesData)))

          const totalValues = map(prop('total'), flatten(map(values, propOr('', [category], allCategoriesData))))
          const averageValues = map(prop('average'), flatten(map(values, propOr('', [category], allCategoriesData))))
          const totalOrAverage = value === 'total' ? totalValues : averageValues

          const result = []
          for (let i = 0; i < years.length; i++) {
            const dataToPush = {x: years[i], y: totalOrAverage[i]}
            result.push(dataToPush)
          }
          return result
        }

         return ({
           yearsForSelectedCategory: flatten(map(keys, pathOr('', [category], allCategoriesData))),
           totalExpensesForSelectedCategory: map(prop('total'), flatten(map(values, propOr('', [category], allCategoriesData)))),
           averageExpensesForSelectedCategory: map(prop('average'), flatten(map(values, propOr('', [category], allCategoriesData)))),
           totalDataForD3: [{
             label: category,
             values: generateDataForD3(category, 'total')
           }],
           averageDataForD3: [{
             label: category,
             values: generateDataForD3(category, 'average')
           }],
           currentCategory: category,
           toggledDataForD3: toggledData
         })
       }
    }

  )
 )

 export default enhance(ByCategory)
