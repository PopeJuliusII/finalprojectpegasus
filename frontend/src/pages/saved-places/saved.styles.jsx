import styled from 'styled-components';
import myImage from '../../assets/lib3.jpg';

export const SavedPageContainer = styled.div`
    height: calc(100vh - 135px);
    width: 100%;
    display: flex;
    border: 1px solid;
    overflow: hidden;
`;

export const SavedImageContainer = styled.div`
    height: 100%;
    width: 75%;
    overflow: hidden;
`;

export const SavedPageMapContainer = styled.div`
    height: 100%;
    width: 100%;
    background-image: url(${myImage});
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    border: 1px solid;
    transition: 6s;
    &:hover {
          cursor: pointer;
          transform: scale(1.1);
          transition: transform 6s cubic-bezier(0.25, 0.45, 0.45, 0.95);
          overflow: hidden
`;

export const SavedPlacesContainer = styled.div`
    height: 100%;
    width: 33%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid;
    overflow: scroll;
`;
