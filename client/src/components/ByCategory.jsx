
import React from 'react'
import ReactDOM from 'react-dom'

function ByCategory ({ categories }) {

  if (!categories) {
    return (
      <p>No data available</p>
    )
  }

  function handleOnChange(event) {

  }
  return (
    <div>
      <h1>Annual expenses for a selected category</h1>
      <select onChange={handleOnChange}>
        {categories.map((category) =>
          <option value={category}>{category}</option>
        )}
      </select>
      
    </div>
  )
}

 export default ByCategory
