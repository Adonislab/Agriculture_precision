import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
} from "react-router-dom";
import Analyse from '';
import Chat from '';
import Skill from '';
import Learn from '';
import Ecommerce from '';
import Api from '';


export default function HomePage() {
  return (
    <Router>
         <Switch>

            <Route path='/'><h3>Acceuil</h3></Route>
            <Route path='/analyse' component={Analyse}><h3>Analyse</h3></Route>
            <Route path='/chat' component={Chat}><h3>Discussion</h3></Route>
            <Route path='/skill' component={Skill}><h3>Détection de maladie</h3></Route>
            <Route path='/learn' component={Learn}><h3>Apprendre</h3></Route>
            <Route path='/commerce' component={Ecommerce}><h3>E-commerce</h3></Route>
            <Route path='/ingenieur' component={Api}><h3>Développeur</h3></Route>

            
         </Switch>
    </Router>
  )
}
