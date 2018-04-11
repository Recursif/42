 React bindings are not included in Redux by default. You need to install them explicitly.

Designing Component Hierarchy

Remember how we designed the shape of the root
state object?
It s time to design the UI hierarchy to match it.

This is not Redux-specific task.
Thiinking in React is a great tutorial that explains the process.

Our design brief is simple.
We want to show a list of todo items.
On click, a todo item is crossed out as completed.
We want to show a field where the user may add a new todo.


Implementing Container Components

Now it s time to hook up those presentional components to Redux by
creating some containers. Technically, a container component is just a react
component that uses store.subsribe() to read a part of the Redux State
tree and supply props to a presentational component it renders.

const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    case 'SHOW_COMPLETED':
      return todos.filter(t => t.completed)
    case 'SHOW_ACTIVE':
      return todos.filter(t => t.completed)
    case 'SHOW_ALL':
    default:
      return todos
  }
}

const mapStateToProps = state => {
  return {
    todos: getVisibleTodos(state.todos, state.visibilityFilter)
  }
}


const mapDispatchToProps = dispatch => {
  return {
    onTodoClick: id => {
      dispatch(toggleTodo(id))
    }
  }
}

import { connect } from 'react-redux'
 
const VisibleTodoList = connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoList)
 
export default VisibleTodoListF
