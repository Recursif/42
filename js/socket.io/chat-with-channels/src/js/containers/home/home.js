
import React, { Component } from 'react'
import { connect } from 'react-redux'
import { Layout, Menu, Breadcrumb, List } from 'antd';

const { Header, Content, Footer } = Layout;

import { fetchChannels } from '../../redux/actions/channels'
import AddChannel from '../../components/add-channel'


class Home extends Component {
    constructor(props) {
        super(props)
    }

    componentWillMount() {
        this.props.dispatch(
            fetchChannels()
        )
    }

    render() {
        return (
            <div>
                <Content style={{ "padding": "50px 50px", "maxWidth": "600px", "margin": "auto" }}>
                    <List
                        span={4}
                        size="large"
                        header={<div style={{ "textAlign": "center" }}>Channels</div>}
                        footer={<div style={{ "textAlign": "center" }}><AddChannel/></div>}
                        bordered
                        dataSource={this.props.channels}
                        renderItem={item => (<List.Item key={item._id}>{item.name}</List.Item>)}
                    />
                </Content>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return state
}

export default connect(mapStateToProps)(Home)