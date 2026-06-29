import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout.jsx'
import Dashboard from './pages/Dashboard.jsx'
import CampaignCreator from './pages/CampaignCreator.jsx'
import EmailComposer from './pages/EmailComposer.jsx'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="campaign" element={<CampaignCreator />} />
          <Route path="email" element={<EmailComposer />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
