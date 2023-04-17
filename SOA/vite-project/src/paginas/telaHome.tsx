
export function Home() {
  const handleIrAoLogin = () => {
    // Redireciona para a tela de pagamento com os dados do pedido
    window.location.href = `/login`;
  };
  const handleIrAoCadastro = () => {
    // Redireciona para a tela de pagamento com os dados do pedido
    window.location.href = `/cadastro`;
  };
    return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' ,background:'#f5f5dc'}}>
      <div style={{ padding: '20px' }}>
        <h1 style={{ textAlign: 'center' }}>CantinaCIN</h1>
        <div style={{ textAlign: 'center' }}>
          <button onClick={handleIrAoLogin} style={{ marginRight: '20px' }}>Login</button>
          <button onClick={handleIrAoCadastro}>Cadastro</button>
        </div>
      </div>
    </div>
    )
}

