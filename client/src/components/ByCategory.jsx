
import React from 'react'
import ReactDOM from 'react-dom'

function ByCategory ({
  categories,
  allCategoriesData,
  showDataForCategory,
  yearsForSelectedCategory,
  totalExpensesForSelectedCategory,
  averageExpensesForSelectedCategory
}) {

  if (!categories) {
    return (
      <p>No data available</p>
    )
  }

  function handleOnChange(event) {
    const selectedCategory = event.target.value
    return showDataForCategory(allCategoriesData, selectedCategory)
  }
  return (
    <div>
      <h1>Annual expenses for a selected category</h1>
      <select onChange={handleOnChange}>
        {categories.map((category) =>
          <option value={category}>{category}</option>
        )}
      </select>
      {yearsForSelectedCategory && <p>total dataForSelectedCategory: {yearsForSelectedCategory}, {totalExpensesForSelectedCategory}</p>}
      {yearsForSelectedCategory && <p>average dataForSelectedCategory: {yearsForSelectedCategory}, {averageExpensesForSelectedCategory}</p>}

    </div>
  )
}

 export default ByCategory
