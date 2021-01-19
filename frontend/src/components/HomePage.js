import React, {Component, component} from "react"

export default class HomePage extends  Component{
    constructor(props){
        super(props);
        this.state={
            items:[],
            tags:'',
            owner:'',
        }
        this.getItems();
        
    }
    getItems(){
        fetch('/api/items').then((respone)=> 
        respone.json()
        ).then((data)=>{
            this.setState({
                items: data
            })
            console.log(data)
        });
    }

    render(){
        return <dv>
            {this.state.items.map((item)=>(
                <div>
                    <h2>{item.title}</h2>
                    <h4>{item.price}$</h4>
                    <h5>{item.tags[0].tag}</h5>
                    <p>{item.description}</p>                    
                    <p>{item.owner.username}</p>                    
                </div>
            ))}
        </dv>
    }
}