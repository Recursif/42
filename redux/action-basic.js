/*
Actions are payloads of information that send data from your app to your store.
They are the only source of information for the store.
You send them to the store using.
store.dispatch().
*/

const ADD_TODO = 'ADD_TODO'

{
  type: ADD_TODO,
  text: 'Build my first Redux app'
}

/*
Actions are Js Objects
*/

import { ADD_TODO, REMOVE_TODO } from '../actionTypes'

{
  type: TOGGLE_TODO,
  index: 5
}

{
  type: SET_VISIBILITY_FILTER,
  filter: SHOW_COMPLETED
}

/* Action creators

Action creators are functions that create actions.
*/

function addTodo (text) {
  return {
    type: ADD_TODO,
    text
  }
}

// to dispatch
dispatch(addTodo(text))
dispatch(completeTodo(index))

// to bound action creator
const boundAddTodo = text => dispatch(addTodo(text))
const boundCompleteTodo = index => dispatch(completeTodo(index))
