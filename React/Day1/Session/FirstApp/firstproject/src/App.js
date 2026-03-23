import logo from './logo.svg';
//import './App.css';
import BasicElement from './components/basic';
import ConditionalRendering from './components/condition';
import ListRendering from './components/ListRendering';
import { Increment } from './components/increment';
import { PageLoad } from './components/pageLoad';
import FocusInput from './components/focus';
import Spread from './components/Spread';

function App() {
  return (
    <div>
      <h1>Welcome to React JS</h1>
      <BasicElement />
      <ConditionalRendering isLoggedIn={true} />
      <ListRendering items={['Apple', 'Banana', 'Cherry']} />
      <Increment />
      {/* <PageLoad /> */}
      <FocusInput />
      <Spread name="John" age={30} city="New York" country="USA" />
    </div>
  );
}

export default App;
