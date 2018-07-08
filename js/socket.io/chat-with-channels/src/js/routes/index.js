
import Home from '../containers/home/home'
import Channel from '../containers/channel/channel'


const routes = [
    {
        path: '/',
        exact: true,
        component: Home,
    },
    {
        path: '/channel/:id',
        component: Channel,
    },
]

export default routes