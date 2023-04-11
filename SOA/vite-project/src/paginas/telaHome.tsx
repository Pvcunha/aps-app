export function Home() {

    return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <div style={{ background:'#f5f5dc', padding: '20px' }}>
        <h1 style={{ textAlign: 'center' }}>CantinaCIN</h1>
        <div style={{ textAlign: 'center' }}>
          <button style={{ marginRight: '20px' }}>Login</button>
          <button>Cadastro</button>
        </div>
      </div>
    </div>
    )
}

