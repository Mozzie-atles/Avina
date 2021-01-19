import React, { Component, component } from "react"
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom'
import { render } from "react-dom"
import HomePage from './HomePage'
import Login from './Login'
export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (
        <Router>
            <Switch>
                <Route exact path='/' component={HomePage}/>
                <Route path='/login' component={Login}/>
            </Switch>
        </Router>
        )
    }
}


const appDiv = document.getElementById('app');
render(<App />, appDiv);