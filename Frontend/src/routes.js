import { Route, Routes as BaseRoutes } from 'react-router-dom';
import Contact from './pages/Contact';
import Search from './components/Search';

export default function Routes() {
  return (
    <BaseRoutes>
      <Route path="/" element={<Search />} />
      <Route path="contact">
        <Route index element={<Contact />} />
      </Route>
    </BaseRoutes>
  );
}
