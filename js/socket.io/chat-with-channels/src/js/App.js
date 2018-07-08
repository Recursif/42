
import React, { Component } from 'react'

import RouteWithSubRoutes from './components/route-with-sub-routes'

import routes from './routes/index.js'


import 'antd/dist/antd.css';

class App extends Component {
    render () {
        return (
            <div>
                {routes.map((route, i) => <RouteWithSubRoutes key={i} {...route} />)}
            </div>
        )
    }
}

export default App