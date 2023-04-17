import { useState, useEffect } from 'react';
import { Item } from '../entidades/Item';
import { Produto } from '../entidades/Produto';
import axios from 'axios';
import { PegarProduto } from '../services/produto';
import { Await } from 'react-router-dom';


export const TelaProdutos : React.FC = () => {

    const [itens, setItens] = useState<Item[]>([]);
    const [carrinho, setCarrinho] = useState<Item[]>([]);

    const addItemCarrinho = (produto: Produto, qtd: number, qtdEstoque: number) => {
        const indexProduto = carrinho.findIndex((item) => item.produto.id == produto.id)
        if (indexProduto >= 0) {
            const carrinhoAtualizado = [...carrinho]
            if((carrinhoAtualizado[indexProduto].qtd + qtd) <= qtdEstoque)
                carrinhoAtualizado[indexProduto].qtd += qtd
            setCarrinho(carrinhoAtualizado)
        } else {
            let item: Item = {produto, qtd} as Item;
            setCarrinho([...carrinho, item]);
        }
    }

    useEffect(() => {
      const fetchItems = async () => {
        const response = await axios.get<Item[]>('http://localhost:3002/listaItens');
        setItens(response.data)
      };
      fetchItems();
      console.log(itens)
    }, []);
    return (
      <div>
        <h1>Produtos:</h1>
        <ul>
            {itens.map(item => (
                <li key={item.produto.id}>
                    nome: {item.produto.nome} - valor: R${item.produto.valor} - Estoque: {item.qtd}
                    <button onClick={() => addItemCarrinho(item.produto, 1, item.qtd)}>Add Carrinho</button>
                </li>
            ))}
        </ul>
        <h1>Carrinho</h1>
        <ul>
            {carrinho.map((item) => (
            <li key={item.produto.nome}>
                {item.produto.nome} - ${item.produto.valor} x {item.qtd}
            </li>
            ))}
      </ul>
      <p>total: R${carrinho.reduce((acc, current) => acc + (current.produto.valor*current.qtd), 0)}</p>
      </div>
    );
}