import { Route, Routes as BaseRoutes } from 'react-router-dom';
import Wrapper from './components/Wrapper';
import Search from './components/Search';
import Contact from './pages/Contact';
import About from './pages/About';

function App() {
  return (
    <div className="App">
      <Wrapper>
        <BaseRoutes>
          <Route path="/" element={<Search />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/about" element={<About />} />
        </BaseRoutes>
      </Wrapper>
    </div>
  );
}

export default App;
