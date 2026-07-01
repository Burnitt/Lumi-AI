import { Outlet, NavLink, useLocation } from 'react-router-dom'
import styles from './Layout.module.css'

const nav = [
  { to: '/',         label: 'Dashboard',  icon: '⌂' },
  { to: '/campaign', label: 'Campaigns',  icon: '◈' },
  { to: '/email',    label: 'Emails',     icon: '✉' },
]

export default function Layout() {
  return (
    <div className={styles.shell}>
      <aside className={styles.sidebar}>
        <div className={styles.brand}>
          <span className={styles.brandMark}>L</span>
          <span className={styles.brandName}>Lumi AI</span>
        </div>

        <nav className={styles.nav}>
          {nav.map(({ to, label, icon }) => (
            <NavLink
              key={to}
              to={to}
              end={to === '/'}
              className={({ isActive }) =>
                `${styles.navItem} ${isActive ? styles.active : ''}`
              }
            >
              <span className={styles.navIcon}>{icon}</span>
              <span>{label}</span>
            </NavLink>
          ))}
        </nav>

        <div className={styles.sidebarFooter}>
          <div className={styles.plan}>
            <span className={styles.planDot} />
            <span>Free plan</span>
          </div>
        </div>
      </aside>

      <main className={styles.main}>
        <Outlet />
      </main>
    </div>
  )
}

