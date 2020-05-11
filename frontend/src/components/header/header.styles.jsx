import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const HeaderContainer = styled.div`
    height: 70px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 25px;
`;

export const LogoContainer = styled(Link)`
    height: 100%;
    width: 70px;
    padding: 25px;
    &:hover {
        cursor: pointer;
        transform: scale(1.2, 1.2) translate(16%, -8.75%);
        transition: transform 0.25s;
}
`;

export const OptionsContainer = styled.div`
    width: 50%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
`;

export const OptionLink = styled(Link)`
    padding: 10px 15px;
    cursor: pointer;
    &:hover {
        cursor: pointer;
        background-color: #E2E2E2;
        transition: 2s ease;
    }
`;
