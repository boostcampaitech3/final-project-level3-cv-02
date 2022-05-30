import React, { Component } from 'react';
import { Link } from "react-scroll";
import './TommMain.css';
import main_image from '../img/main_sketch.png';
import main_logo from '../img/main_logo.png';
import dot from '../img/navi_dot.png';

class TommMain extends Component {
  constructor(props){
    super(props);
    this.state={
      button_mouseover_count: 0
    }
    this.MouseOverHandler = this.MouseOverHandler.bind(this);
  }
  MouseOverHandler(e) {
    e.preventDefault();
    this.setState({button_mouseover_count: 1});
  }
    render() {
      const main_text = 'PERSONAL INTERIOR\nCONSULTING';
      const sub_text = 'CV-02 Bucket-Interior';
      const button_text = 'Start'

      return (
        <div className="Main-background" id="scroll_to_main">
          <img src={main_logo} className="Main-Logo" alt=""></img>
          <img src={main_image} className="Main-Image" alt=""></img>
          <div className="Main-Text-Div-01">
            <p className="Main-Text-01">{main_text}</p>
          </div>
          <div className="Main-Text-Div-02">
            <p className="Main-Text-02">{sub_text}</p>
          </div>
          <Link to="scroll_to_upload" spy={true} smooth={true}>
            <div className="Main-Button-Div-01">
              <button 
              className={(this.state.button_mouseover_count===0)? "Main-Button-01" : "Main-Button-01-after"}
              onMouseOver={this.MouseOverHandler}
              >{button_text}</button>
            </div>
          </Link>
          <div className="scroll-downs">
            <div className="mousey">
              <div className="scroller"></div>
            </div>
          </div>
          <ul className="Main-navi">
            <Link to="scroll_to_main" spy={true} smooth={true}>
            <li><img 
                  src={dot} 
                  className={(this.props.percent<0.8) ? "Main-dot-current" : "Main-dot"}
                  alt=""></img></li>
            </Link>
            <Link to="scroll_to_intro" spy={true} smooth={true}>
            <li><img 
                  src={dot} 
                  className={(0.8<this.props.percent && this.props.percent<3.1) ? "Main-dot-current" : "Main-dot"}
                  alt=""></img></li>
            </Link>
            <Link to="scroll_to_result" spy={true} smooth={true}>
            <li><img 
                  src={dot} 
                  className={(3.1<this.props.percent && this.props.percent<4.2) ? "Main-dot-current" : "Main-dot"}
                  alt=""></img></li>
            </Link>
            <Link to="scroll_to_upload" spy={true} smooth={true}>
            <li><img 
                  src={dot} 
                  className={(4.2<this.props.percent) ? "Main-dot-current" : "Main-dot"}
                  alt=""></img></li>
            </Link>
          </ul>
        </div>
      );
    }
}

export default TommMain;