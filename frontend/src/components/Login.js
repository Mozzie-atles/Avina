import React, {Component, component} from "react"

export default class Login extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return <from method="POST" class="from-group">
            {{csrf_token}}
                    <label>Login</label>
                <div>
                    <input placeholder="Username" name='username'/>
                </div>
                <div>
                    <input placeholder="Password" name='password'/>
                </div>
                <button type='submit'>Login</button>
            </from>
        
    }
}