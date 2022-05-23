import React, { Component } from 'react';
import './PageIntro.css';
import rhombus from '../img/rhombus.png';
import logo_mix from '../img/logo_mix.png';

class PageIntro extends Component {
    render() {
      return (
        <div className="Intro-background">
          <div className="Intro-block block-01">
            <div className={(400<this.props.scroll_y && this.props.scroll_y<1100) ? "Intro-block-left left-01" : "Intro-block-left-hidden"}>
              <img src={logo_mix} className="Intro-logo-mix" alt=""></img>
            </div>
            <div className={(400<this.props.scroll_y && this.props.scroll_y<1100) ? "Intro-block-right right-01" : "Intro-block-right-hidden"}>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <h1 className="Intro-Text-01">Draw what you want</h1>
              <hr/>
              <p>
                내 방 사진을 찍고 
                <br/>원하는 모습대로 스케치해보세요!
              </p>
            </div>
          </div>
          <div className="Intro-block block-02">
            <div className={(900<this.props.scroll_y && this.props.scroll_y<1600) ? "Intro-block-left left-02" : "Intro-block-left-hidden"}>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <h1 className="Intro-Text-01">Upload your room</h1>
              <hr/>
              <p>
                스케치를 추가하기 전, 후 사진
                <br/>총 2장을 업로드해주세요
              </p>
            </div>
            <div className={(900<this.props.scroll_y && this.props.scroll_y<1600) ? "Intro-block-right right-02" : "Intro-block-right-hidden"}>
              <img src={logo_mix} className="Intro-logo-mix" alt=""></img>
            </div>
          </div>
          <div className="Intro-block block-03">
          <div className={(1500<this.props.scroll_y && this.props.scroll_y<2200) ? "Intro-block-left left-03" : "Intro-block-left-hidden"}>
              <img src={logo_mix} className="Intro-logo-mix" alt=""></img>
            </div>
            <div className={(1500<this.props.scroll_y && this.props.scroll_y<2200) ? "Intro-block-right right-03" : "Intro-block-right-hidden"}>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <img src={rhombus} className="Intro-Rhombus" alt=""></img>
              <h1 className="Intro-Text-01">AI will makes it a reality</h1>
              <hr/>
              <p>
                AI가 새롭게 방을 꾸며줄때까지 잠시 기다려주세요
                <br/>1시간 후에 메일로 보내드립니다
              </p>
            </div>
          </div>
        </div>
      );
    }
}

export default PageIntro;