using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using LHPet.Models;

namespace LHPet.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        Cliente cliente1 = new Cliente(1, "Nome1", "111.111.111-11", "email1@email.com", "Cachorro");
        Cliente cliente2 = new Cliente(2, "Nome2", "111.111.111-11", "email2@email.com", "Cachorro");
        Cliente cliente3 = new Cliente(3, "Nome3", "111.111.111-11", "email3@email.com", "Cachorro");
        Cliente cliente4 = new Cliente(4, "Nome4", "111.111.111-11", "email4@email.com", "Cachorro");
        Cliente cliente5 = new Cliente(5, "Nome5", "111.111.111-11", "email5@email.com", "Cachorro");

        List<Cliente> listaClientes = new List<Cliente>();
        listaClientes.Add(cliente1);
        listaClientes.Add(cliente2);
        listaClientes.Add(cliente3);
        listaClientes.Add(cliente4);
        listaClientes.Add(cliente5);

        ViewBag.listaClientes = listaClientes;


        Fornecedor fornecedor1 = new Fornecedor(1, "Nome1", "CNPJ", "email@email.com");
        Fornecedor fornecedor2 = new Fornecedor(2, "Nome2", "CNPJ", "email@email.com");
        Fornecedor fornecedor3 = new Fornecedor(3, "Nome3", "CNPJ", "email@email.com");
        Fornecedor fornecedor4 = new Fornecedor(4, "Nome4", "CNPJ", "email@email.com");
        Fornecedor fornecedor5 = new Fornecedor(5, "Nome5", "CNPJ", "email@email.com");
        
        List<Fornecedor> listaFornecedores = new List<Fornecedor>();
        listaFornecedores.Add(fornecedor1);
        listaFornecedores.Add(fornecedor2);
        listaFornecedores.Add(fornecedor3);
        listaFornecedores.Add(fornecedor4);
        listaFornecedores.Add(fornecedor5);

        ViewBag.listaFornecedores = listaFornecedores;

        return View();
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
