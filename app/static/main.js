

// ---------- TELA ADMIN -------------

// exibe modal com cadastro escola
$(function () {
    $(".btn-add-escola").click(function (e) {
        e.preventDefault();
        const el = $(this).data('element');
        $(el).toggle();
    });
  });


  // exibe modal com cadastro escola
  

  
  
  // exibe modal com cadastro curso
  $(function () {
    $(".btn-add-curso").click(function (e) {
        e.preventDefault();
        const el = $(this).data('element');
        $(el).toggle();        
    });
  });
  
  // exibe modal com cadastro curso
  $(function () {
    $(".btn-add-equipe").click(function (e) {
        e.preventDefault();
        const el = $(this).data('element');
        $(el).toggle();        
    });
  });
  

  
  // exibe tabela com informacoes da perfil selecionada
  $(function () {
    $(".btn-dados-usuario").click(function (e) {
        
        const el = $(this).data('element');
        $(el).toggle();       
    });
  });
  
  
  // exibe criar usuario
  $(function () {
    $(".btn-criar-usuario").click(function (e) {
        e.preventDefault();
        const el = $(this).data('element');
        $(el).toggle();       
    });
  });
  
  
  
  // oculta tabela aberta ao clicar nas abas Escola, Equipe e Acervo
  const linkTable = document.querySelectorAll('.nav_link_table')
  
  
  function tableLink() {
    if (linkTable) {
        linkTable.forEach(function (l) {
            const el = $(l).data('element');
            $(el).hide();
        }
    )}
  }
  linkTable.forEach(l => l.addEventListener('click', tableLink))
  
  
  
  
  
  // remove item da turma
  const RemoveTurma = () => {
    $(".btn-del-turma-equipe").click(function  (e) {
        e.preventDefault();
        this.parentNode.remove(this.parentNode);
    });
  }
  
  
  
  
  // inseri nova linha para incluir turma ao colaborador
  $(function () {
    $(".btn-add-turma-equipe").click(function (e) {
        e.preventDefault();
        $(".equipe-list-turma").append('<li class="list-group-item d-flex justify-content-between">' + 
        '<select class="custom-select mr-2 border-0" id="diaDaSemana">'+
        '<option selected>Nome da Turma</option>'+
        '<option value="1">Violão Básico I - Belo Horizonte</option>'+
        '<option value="2">Violino Básico I - Betim</option>'+
        '<option value="3">Saxofone Básico I - Contagem</option>'+
        '</select>'+ 
        '<a class="btn-del-turma-equipe my-auto "><i class="fa-solid fa-lg fa-delete-left text-muted"></i></a>'+
    '</li>');
        RemoveTurma();
    });
  });
  
  
  
  // remove item da turma
  const RemoveInstrumento = () => {
    $(".btn-del-instrumento-equipe").click(function  (e) {
        e.preventDefault();
        this.parentNode.remove(this.parentNode);
    });
  }
  
  
  
  
  // inseri nova linha para incluir instrumentos ao colaborador
  $(function () {
    $(".btn-add-instrumento-equipe").click(function (e) {
        e.preventDefault();
        $(".equipe-list-instr").append('<li class="list-group-item d-flex justify-content-between">' + 
        '<select class="custom-select mr-2 border-0" id="diaDaSemana">'+
        '<option selected>Nome do Instrumento</option>'+
        '<option value="1">Violão</option>'+
        '<option value="2">Violino</option>'+
        '<option value="3">Saxofone</option>'+
        '</select>'+ 
        '<a class="btn-del-instrumento-equipe my-auto "><i class="fa-solid fa-lg fa-delete-left text-muted"></i></a>'+
    '</li>');
        RemoveInstrumento();
    });
  });
  
  
  
  // ----------- TELA ALUNO --------------
  
  // exibe modal com cadastro aluno
  $(function () {
    $(".btn-add-aluno").click(function (e) {
        e.preventDefault();
        const el = $(this).data('element');
        $(el).toggle();        
    });
  
  
  
  // exibe tabela com informacoes do membro da equipe selecionado
  // $(function () {
  //   $(".open-info-aluno").click(function (e) {
  //       const el = $(this).data('element');
  //       $(el).toggle();       
  //   });
  // });
    $(".open-info-aluno").click(function (e) {              
      e.preventDefault();
      const el = $(this).data('element');
      $(el).toggle();
      const id = $(this).data('id');
      console.log(id)
      $.ajax({        
        type: "GET",
        url: "/alunos/" + id,
        success: function(response){
          console.log(response)
          //debugger
          $('#nomeAluno-modal-selecao').val(response.nome)
          $('#dataNascimento-modal-selecao').val(response.data_nascimento)
          $('#enderecoAluno-modal-selecao').val(response.endereco)
          $('#email-modal-selecao').val(response.email)
          $('#telefone-modal-selecao').val(response.telefone)
          $('#nomeResponsavel-modal-selecao').val(response.nome_resp)
          $('#telefoneResponsavel-modal-selecao').val(response.telefone_resp)
          $('#emailResponsavel-modal-selecao').val(response.email_resp)
          $('#turmaAluno-modal-selecao').val(response.turma)
          $('#instrumentoAluno-modal-selecao').val(response.instrumento)
          $('#dataMatricula-modal-selecao').val(response.data_admissao)
          $('#anotacoes').val(response.anotacoesAluno)
          $('#dataDesligamento-modal-selecao').val(response.data_desligamento)

          $('.btn-edit-aluno').attr('href', "/aluno/cadastro/" + response.id)
        }        
      });
  });
});
  
  
  
  // ----------- TELA INSTRUMENTO --------------
  
  // exibe modal com cadastro instrumento
  $(function () {
    $(".btn-add-instrumento").click(function (e) {
      e.preventDefault();
      const el = $(this).data("element");
      $(el).toggle();
    });

  // exibe modal com cadastro tipo de instrumento
    $(".btn-add-tipo-instrumento").click(function (e) {
      e.preventDefault();
      const el = $(this).data("element");
      $(el).toggle();
    });
  
  
  
    $(".btn-emp-instrumento").click(function (e) {
      e.preventDefault();
      const el = $(this).data("element");
      $(el).toggle();
    });
  });
  
  
  
  
  
  
  