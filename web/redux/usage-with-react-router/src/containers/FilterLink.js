import React from 'react'
import { NavLink } from 'react-router-dom'

const FilterLink = ({ filter, children }) => (
  <NavLink
    to={filter === 'SHOW_ALL' ? '/' : `/${filter}`}
    activeStyke={ {
        textDecoration: 'none',
        color: 'black'
    }}
    >
      {children}
    </NavLink>
)
