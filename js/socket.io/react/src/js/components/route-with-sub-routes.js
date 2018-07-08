
import React from 'react'
import { Route } from 'react-router-dom'

const RouteWithSubRoutes = route => (
    <Route
        path={route.path}
        exact={route.exact}
        render={props => (
            // Pass the sub-routes down to keep nesting
            <route.component {...props} routes={route.routes} />
        )}
    />
)

export default RouteWithSubRoutes