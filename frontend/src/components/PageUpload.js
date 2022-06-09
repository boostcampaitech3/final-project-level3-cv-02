import React, { Component } from 'react';
import './PageUpload.css';
import axios from 'axios';
import {ToastsContainer, ToastsStore, ToastsContainerPosition} from 'react-toasts';
import PageModal from "./PageModal.js"
import file_upload_img from '../img/file_upload_img.png';
import logo_brown from '../img/logo_brown.png';

class PageUpload extends Component {
    constructor(props){
      super(props);
      this.state={
        email: '',
        original_image_file: null,
        sketch_image_file: null,
        original_image_url: file_upload_img,
        sketch_image_url: file_upload_img,
        original_image_width: null,
        original_image_height: null,
        sketch_image_width: null,
        sketch_image_height: null,
        showModal: false
      };
      this.inputEmailHandler = this.inputEmailHandler.bind(this);
      this.inputImageHandler = this.inputImageHandler.bind(this);
      this.inputSubmitHandler = this.inputSubmitHandler.bind(this);
      this.ModalHandler = this.ModalHandler.bind(this);
      this.ModalCloseHandler = this.ModalCloseHandler.bind(this);
    }
    ModalHandler(e) {
      e.preventDefault();
      this.setState({showModal: true});
      document.body.style.overflow = "hidden";
    }
    ModalCloseHandler(e) {
      e.preventDefault();
      this.setState({showModal: false});
      document.body.style.overflow = "unset";
    }
    modalExitHandler(e) {
      e.preventDefault();
      alert('s');
    }
    inputEmailHandler(e) {
      e.preventDefault();
      this.setState({email: e.target.value})
    }
    inputImageHandler(e) {
      e.preventDefault();
      var file = e.target.files[0];
      var target_name = e.target.name + '_url';
      var file_name = e.target.name + '_file';
      var width_name = e.target.name + '_width';
      var height_name = e.target.name + '_height'
      var new_url = URL.createObjectURL(file);
      var img = new Image();
      img.src = new_url;
      img.onload = function() {
        this.setState({
          [target_name]: new_url,
          [file_name]: file,
          [width_name]: img.width,
          [height_name]: img.height
        });
      }.bind(this);
    }
    inputSubmitHandler(e) {
      e.preventDefault();
      let original_img_url = this.state.original_image_url;
      let sketch_img_url = this.state.sketch_image_url;
      let current_time = new Date();
      let time = {
        year: current_time.getFullYear(),
        month: ("0"+(current_time.getMonth()+1)).slice(-2),
        date: ("0"+current_time.getDate()).slice(-2),
        hours: ("0"+current_time.getHours()).slice(-2),
        minutes: ("0"+current_time.getMinutes()).slice(-2),
        seconds: ("0"+current_time.getSeconds()).slice(-2),
      };
      let timestring = `${time.year}-${time.month}-${time.date}_${time.hours}:${time.minutes}:${time.seconds}`;
      // eslint-disable-next-line
      let email_format = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;

      if (this.state.original_image_file===null) { 
          ToastsStore.success("원본 이미지를 업로드해주세요");
       }
      else if (this.state.sketch_image_file===null) {
          ToastsStore.success("스케치 이미지를 업로드해주세요");
      }
      else if (this.state.email==='') {
          ToastsStore.success("이메일을 입력해주세요");
      }
      else if (email_format.test(this.state.email)===false) {
        ToastsStore.success("이메일 형식이 올바르지 않습니다");
      }
      else {
        const data = new FormData();
        var host = 'http://localhost:8000/';

        data.append('submit_original_img', this.state.original_image_file);
        data.append('submit_sketch_img', this.state.sketch_image_file);
        data.append('submit_email', this.state.email);
        data.append('original_image_width', this.state.original_image_width);
        data.append('original_image_height', this.state.original_image_height);
        data.append('sketch_image_width', this.state.sketch_image_width);
        data.append('sketch_image_height', this.state.sketch_image_height);
        data.append('upload_time', timestring);

        axios.post(host, data, {
          onUploadProgress: ProgressEvent => {
            this.setState({
              loaded: (ProgressEvent.loaded / ProgressEvent.total*100),
            })
          },
        }) 
        ToastsStore.success("업로드 완료 :) 1시간 뒤 메일함을 확인해주세요!");
      
        this.setState({
          email: '',
          original_image_file: null,
          sketch_image_file: null,
          original_image_url: file_upload_img,
          sketch_image_url: file_upload_img,
          original_image_width: null,
          original_image_height: null,
          sketch_image_width: null,
          sketch_image_height: null
        });
        URL.revokeObjectURL(original_img_url);
        URL.revokeObjectURL(sketch_img_url);
      }
    }

    render() {
      return (
        <div 
          className={(this.props.percent > 3.8) ? "Upload-background" : "Upload-background-ani"}
          id="scroll_to_upload">
          <img src={logo_brown} className="Upload-logo" alt=""></img>
          <h2 className="Upload-background-title">내일의 집 꾸며보기</h2>
          <div>
            <button className="Upload-guideline" onClick={this.ModalHandler}>Guideline</button>
          </div>
          {this.state.showModal ? (
            <PageModal 
              showModal={this.state.showModal}
              closeHandler={this.ModalCloseHandler}>
            </PageModal>) : null}
          <form 
            className="Upload-form"
            action="/" 
            method="post"
            onSubmit={this.inputSubmitHandler}>

            <div className="Upload-original">
              <h2 className="Upload-title">원본 사진</h2>
              <label id="Upload-original-sub" htmlFor="Upload-original-button">
                <img src={this.state.original_image_url} className="File-upload-img" alt=""></img>
              </label>
              <input 
                type="file"
                id="Upload-original-button"
                accept="image/*"
                name='original_image'
                onChange={this.inputImageHandler}>
              </input>
            </div>
            <div className="Upload-sketch">
              <h2 className="Upload-title">스케치 사진</h2>
              <label id="Upload-sketch-sub" htmlFor="Upload-sketch-button">
                <img src={this.state.sketch_image_url} className="File-upload-img" alt=""></img>
              </label>
              <input 
                type="file"
                id="Upload-sketch-button"
                accept="image/jpg, image/jpeg, image/png"
                name='sketch_image'
                onChange={this.inputImageHandler}>
              </input>
            </div>
            <input
              className="Upload-email"
              type="text"
              placeholder={'이메일을 입력하세요'}
              value={this.state.email}
              onChange={this.inputEmailHandler}
            ></input>
            <input
              className="Upload-submit"
              type="submit"
              value="완료"
            ></input>
            <ToastsContainer 
              position={ToastsContainerPosition.BOTTOM_CENTER} store={ToastsStore} lightBackground/>
          </form>
        </div>
      );
    }
}

export default PageUpload;