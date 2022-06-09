import React, { Component } from 'react';
import './PageFooter.css';
import footer_logo from '../img/footer_logo.png';

class PageFooter extends Component {
    render() {
      return (
        <div className={(this.props.percent > 4.8) ? "Footer-background" : "Footer-background-ani"}>
          <div className="Footer-logo">
            <img src={footer_logo} className="Footer-logo-img" alt=""></img>
          </div>
          <div className="Footer-content">
            <p className="Footer-content-01">Boostcamp AI Tech 3기 Final Project</p>
            <p className="Footer-content-02">CV-02조 Bucket-Interior</p>
            <table>
              <tbody>
                <tr>
                  <th>Members</th>
                  <td>김예원</td>
                  <td>김주영</td>
                  <td>유환규</td>
                  <td>이수아</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="Footer-github">
            <button 
              className="Footer-github-button"
              onClick={() => window.open('https://github.com/boostcampaitech3/final-project-level3-cv-02', '_blank')}>
              Project Github
            </button>
          </div>
        </div>
      );
    }
}

export default PageFooter;