import { useState, useEffect } from 'react';
import { Item } from '../entidades/Item';
import { Produto } from '../entidades/Produto';
import axios from 'axios';

export const TelaProdutos: React.FC = () => {
  const [itens, setItens] = useState<Item[]>([]);
  const [carrinho, setCarrinho] = useState<Item[]>([]);

  const addItemCarrinho = (produto: Produto, qtd: number, qtdEstoque: number) => {
    const indexProduto = carrinho.findIndex(
      (item) => item.produto.id === produto.id
    );
    if (indexProduto >= 0) {
      const carrinhoAtualizado = [...carrinho];
      if (carrinhoAtualizado[indexProduto].qtd + qtd <= qtdEstoque)
        carrinhoAtualizado[indexProduto].qtd += qtd;
      setCarrinho(carrinhoAtualizado);
    } else {
      let item: Item = { produto, qtd } as Item;
      setCarrinho([...carrinho, item]);
    }
  };

  const criarPedido = async () => {
    const token = localStorage.getItem("token");
    const decodedToken = JSON.parse(token);
    const { email,id } = decodedToken;
    
    /*
    const usuarioEmail = localStorage.getItem('usuarioEmail');
    const usuarioID = localStorage.getItem('usuarioID');
    const usuarioTipo = localStorage.getItem('usuarioTipo');
  */
    const pedido = {
      produtos: carrinho.map((item) => {
        return {
          nome: item.produto.nome,
          valor: item.produto.valor,
          id: item.produto.id,
          qtd: item.qtd,
        };
      }),
    };
    const body = {
      "usuarioEmail":email,
      "usuarioID":id,
      "usuarioTipo":"Cliente",
      "pedido":pedido,
    };
  
    const response = await axios.post('http://localhost:3030/pedido/criaPedido', body);
    const confirmacao = response.data;  
    console.log(confirmacao)
    if(confirmacao)
        localStorage.setItem("confirmação",JSON.stringify(confirmacao))
        window.location.href = `/pagamento`;
  };


  useEffect(() => {
    const fetchItems = async () => {
      const response = await axios.get<Item[]>('http://localhost:3030/estoque/listaItens');
      setItens(response.data);
    };
    fetchItems();
  }, []);


  return (
    <div style={{ textAlign: 'center' , height: '100vh' , background:'#f5f5dc'}}>
      <h1>Produtos:</h1>
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        {itens.map((item) => (
          <div
            key={item.produto.id}
            style={{
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              alignItems: 'center',
              margin: '20px',
            }}
          >
            <h3>{item.produto.nome}</h3>
            <p>Valor: R${item.produto.valor}</p>
            <p>Estoque: {item.qtd}</p>
            <button onClick={() => addItemCarrinho(item.produto, 1, item.qtd)}>
              Adicionar ao carrinho
            </button>
          </div>
        ))}
      </div>
      <h1>Carrinho</h1>
      <ul>
        {carrinho.map((item) => (
          <li key={item.produto.nome}>
            {item.produto.nome} - ${item.produto.valor} x {item.qtd}
          </li>
        ))}
      </ul>
      <p>
        Total: R$
        {carrinho.reduce(
          (acc, current) => acc + current.produto.valor * current.qtd,
          0
        )}
      </p>
      <button  onClick={criarPedido}>Criar pedido</button>
    </div>
  );
};
