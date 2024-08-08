#!/bin/bash
echo "==== Informações do Sistema ===="
echo "Sistema Operacional:" $(uname)
echo "CPU:" $(lscpu | grep "Nome do modelo")
echo "Memoria Total:" $(free -h | grep "Mem.")
echo "Espaço em Disco Total:" $(df -h --total | grep "total" | awk '/total/{print $2}')
 
echo "==== Informações do Usuário ===="
echo "Nome de Usuário:" $(who | awk '{print $1}')
echo "Diretório Home:" $(echo $HOME)
echo "Diretório Atual:" $(pwd)
echo "Usuários Logados:" $(whoami)