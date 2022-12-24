import {Component} from 'react';
import PropTypes from 'prop-types';

// const Test = ({name, favoriteNumber, children}) => {
//     // const {name, children} = props;
//     return (
//         <div>
//             제 이름은 {name}입니다 <br></br>
//             children 값은 {children}
//             입니다.
//             <br/>
//             제가 좋아하는 숫자는 {favoriteNumber}입니다.
//         </div> 
//     )
// }

// Test.defaultProps = {
//     name: '기본 이름'
// };

// Test.propTypes = {
//     name: PropTypes.string,
//     favoriteNumber: PropTypes.number.isRequired
// };



class Test extends Component {
    static defaultProps = {
        name: '기본이름'
    };

    static propTypes = {
        name: PropTypes.string,
        favoriteNumber: PropTypes.number.isRequired
    };

    render() {
        const { name, favoriteNumber, children } = this.props;
        return (
            <div>
                제 이름은 {name}입니다 <br></br>
                children 값은 {children}
                입니다.
                <br />
                제가 좋아하는 숫자는 {favoriteNumber}입니다.
            </div>
        )
    }
}



export default Test;