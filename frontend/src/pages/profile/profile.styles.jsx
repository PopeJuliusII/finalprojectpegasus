import styled from 'styled-components';
import myImage from '../../assets/ipad.jpg';

export const ProfilePageContainer = styled.div`
    height: calc(100vh - 135px);
    width: 100%;
    display: flex;
    border: 1px solid;
    overflow: hidden;
`;

export const ProfileImageContainer = styled.div`
    height: 100%;
    width: 75%;
    overflow: hidden;
`;

export const ProfilePageMapContainer = styled.div`
    height: 100%;
    width: 100%;
    background-image: url(${myImage});
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    border: 1px solid;
    &:hover {
          cursor: pointer;
          transform: scale(1.1);
          transition: transform 6s cubic-bezier(0.25, 0.45, 0.45, 0.95);
          overflow: hidden
`;

export const ProfilePlacesContainer = styled.div`
    height: 100%;
    width: 33%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid;
    overflow: scroll;
`;
