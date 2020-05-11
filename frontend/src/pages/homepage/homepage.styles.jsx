import styled from 'styled-components';
import myImage from '../../assets/background-image2.jpeg';

export const HomePageContainer = styled.div`
    height: calc(100vh - 135px);
    width: 100%;
    display: flex;
    background-image: url(${myImage});
    background-size: cover;
    border: 1px solid;
    align-items: center;
    justify-content: center;
    overflow: hidden;
`;

export const HomePageImageContainer = styled.div`
    height: calc(100vh - 135px);
    width: 100%;
    display: flex;
    background-image: url(${myImage});
    background-size: cover;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 90px;
    &:hover {
          cursor: pointer;
          transform: scale(1.1);
          transition: transform 6s cubic-bezier(0.25, 0.45, 0.45, 0.95);
          overflow: hidden
          font-size: 50px;
`;
