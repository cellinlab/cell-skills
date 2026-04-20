/**
 * iOS Frame — React component for iPhone device bezel with status bar.
 * Load via: <script type="text/babel" src="ios_frame.jsx"></script>
 *
 * Usage:
 *   <IOSFrame>
 *     <div>Your app screen content here</div>
 *   </IOSFrame>
 */

function IOSFrame({ children, color = '#000', showNotch = true }) {
  // Auto-compute text contrast
  const isLight = color.match(/^#[0-9a-f]{6}$/i)
    ? (() => { const r = parseInt(color.slice(1,3),16), g = parseInt(color.slice(3,5),16), b = parseInt(color.slice(5,7),16); return (r*299+g*587+b*114)/1000 > 128; })()
    : false;
  const textColor = isLight ? '#000' : '#fff';

  const frameStyles = {
    width: '393px',
    height: '852px',
    borderRadius: '50px',
    border: '4px solid #1a1a1a',
    background: color,
    overflow: 'hidden',
    position: 'relative',
    boxShadow: '0 20px 60px rgba(0,0,0,0.3)',
  };

  const statusBarStyles = {
    height: '54px',
    display: 'flex',
    alignItems: 'flex-end',
    justifyContent: 'space-between',
    padding: '0 32px 8px',
    fontFamily: 'system-ui, -apple-system, sans-serif',
    fontSize: '15px',
    fontWeight: 600,
    color: textColor,
  };

  const contentStyles = {
    height: 'calc(100% - 54px)',
    overflow: 'auto',
    position: 'relative',
  };

  const notchStyles = {
    position: 'absolute',
    top: '0',
    left: '50%',
    transform: 'translateX(-50%)',
    width: '126px',
    height: '34px',
    background: '#000',
    borderRadius: '0 0 20px 20px',
    zIndex: 10,
  };

  const homeIndicatorStyles = {
    position: 'absolute',
    bottom: '8px',
    left: '50%',
    transform: 'translateX(-50%)',
    width: '134px',
    height: '5px',
    background: isLight ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.3)',
    borderRadius: '3px',
  };

  const time = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });

  return React.createElement('div', { style: frameStyles },
    showNotch && React.createElement('div', { style: notchStyles }),
    React.createElement('div', { style: statusBarStyles },
      React.createElement('span', null, time),
      React.createElement('div', { style: { display: 'flex', gap: '4px', alignItems: 'center' } },
        React.createElement('span', { style: { fontSize: '13px' } }, '5G'),
        React.createElement('span', null, '87%')
      )
    ),
    React.createElement('div', { style: contentStyles }, children),
    React.createElement('div', { style: homeIndicatorStyles })
  );
}

Object.assign(window, { IOSFrame });
