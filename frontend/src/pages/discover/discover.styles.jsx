import styled from 'styled-components';

export const DiscoverPageContainer = styled.div`
    height: calc(100vh - 135px);
    width: 100%;
    display: flex;
    border: 1px solid;
    overflow: hidden;
`;

export const DiscoverPageMapContainer = styled.div`
    height: 100%;
    width: 75%;
    display: flex;
    align-items: center;
    border: 1px solid;
`

export const DiscoverRecsContainer = styled.div`
    height: 100%;
    width: 25%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid;
    overflow: scroll;
`
