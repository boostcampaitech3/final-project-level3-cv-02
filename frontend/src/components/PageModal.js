import React, { Component } from 'react';
import './PageModal.css';
import "slick-carousel/slick/slick.css"
import "slick-carousel/slick/slick-theme.css"
import Slider from "react-slick";
import close_img from '../img/close.png';
import page_01 from '../img/modal_images/page_01.PNG';
import page_02 from '../img/modal_images/page_02.PNG';
import page_03 from '../img/modal_images/page_03.PNG';
import page_04 from '../img/modal_images/page_04.PNG';
import page_05 from '../img/modal_images/page_05.PNG';

class PageModal extends Component {
    render() {
      const settings = {
        dots: true,
        infinite: true,
        speed: 800,
        arrows: true,
        pauseOnHover: true
      };

      const text_01 = "1. 스케치 영역이 너무 작지 않게 해주세요"
      const text_02 = "2. 스케치는 선으로 그려지지 않게 영역 내부를 모두 색칠해주시고,\n가장자리까지도 반드시 채워주세요"
      const text_03 = "3. 자잘한 인테리어 소품보다는 큰 가구들을 꾸며주세요\n(추천 가구: 침대, 커튼, 벽지 등)"
      const text_04 = "4. 원래 색상과 너무 비슷하지 않은 색으로 채워주세요"
      const text_05 = "5. 원본 사진과 스케치 사진 2장을 자리에 맞게 업로드하면 완료!"

      return (
        <div className="Modal-background">
            <div className="Modal-container">
              <img src={close_img} className="Modal-close" alt="" onClick={this.props.closeHandler}></img>
              <h2 className="Modal-h2">Guideline</h2>
              <hr></hr>
              <Slider {...settings}>
                <div className="Modal-content">
                  <p className="Modal-text">{text_01}</p>
                  <img src={page_01} className="Modal-page-00" alt=""></img>
                </div>
                <div className="Modal-content">
                  <p className="Modal-text">{text_02}</p>
                  <img src={page_02} className="Modal-page" alt=""></img>
                </div>
                <div className="Modal-content">
                  <p className="Modal-text">{text_03}</p>
                  <img src={page_03} className="Modal-page" alt=""></img>
                </div>
                <div className="Modal-content">
                  <p className="Modal-text">{text_04}</p>
                  <img src={page_04} className="Modal-page-02" alt=""></img>
                </div>
                <div className="Modal-content">
                  <p className="Modal-text">{text_05}</p>
                  <img src={page_05} className="Modal-page-00" alt=""></img>
                </div>
              </Slider>
            </div>
        </div>
      );
    }
}

export default PageModal;