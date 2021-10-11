from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Curso, Aula, Comentario, NotaAula
import json


def home(request):
    if request.session.get('usuario'):
        cursos = Curso.objects.all()
        request_usuario = request.session.get('usuario')
        
        return render(request, 'home.html',
                      {'cursos': cursos, 'request_usuario': request_usuario})
                      
    return redirect('/auth/login/?status=2')


def curso(request, id):
    if request.session.get('usuario'):
        v_curso = Curso.objects.get(id=id)
        aulas = Aula.objects.filter(curso=v_curso)
        
        return render(request, 'curso.html',
                      {'curso': v_curso, 'aulas': aulas})

    return redirect('/auth/login/?status=2')


def aula(request, id):
    if request.session.get('usuario'):
        aula = Aula.objects.get(id=id)
        usuario_id = request.session['usuario']
        comentarios = Comentario.objects.filter(aula=aula).order_by('-data')

        request_usuario = request.session.get('usuario')
        usuario_avaliou = NotaAula.objects.filter(
            aula_id=id).filter(usuario_id=request_usuario)
        avaliacoes = NotaAula.objects.filter(aula_id=id)

        return render(request, 'aula.html',     {
            'aula': aula,
            'usuario_id': usuario_id,
            'comentarios': comentarios,
            'request_usuario': request_usuario,
            'usuario_avaliou': usuario_avaliou,
            'avaliacoes': avaliacoes
        })

    return redirect('/auth/login/?status=2')


def comentarios(request):
    usuario_id = int(request.POST.get('usuario_id'))
    comentario = request.POST.get('comentario')
    aula_id = int(request.POST.get('aula_id'))

    comentario_instancia = Comentario(usuario_id=usuario_id,
                                      comentario=comentario,
                                      aula_id=aula_id)
    comentario_instancia.save()

    comentarios = Comentario.objects.filter(aula=aula_id).order_by('-data')
    somente_nomes = [i.usuario.nome for i in comentarios]
    somente_comentarios = [i.comentario for i in comentarios]
    comentarios = list(zip(somente_nomes, somente_comentarios))

    return HttpResponse(json.dumps(
        {'status': '1', 'comentarios': comentarios}))


def processa_avaliacao(request):
    if request.session.get('usuario'):

        avaliacao = request.POST.get('avaliacao')
        aula_id = request.POST.get('aula_id')

        usuario_id = request.session.get('usuario')

        usuario_avaliou = NotaAula.objects.filter(
            aula_id=aula_id).filter(usuario_id=usuario_id)

        if not usuario_avaliou:
            nota_aulas = NotaAula(aula_id=aula_id,
                                  nota=avaliacao,
                                  usuario_id=usuario_id,
                                  )
            nota_aulas.save()

            return redirect(f'/home/aula/{aula_id}')

        return redirect('/auth/login/')

    return redirect('/auth/login/')
