echo 'apagando politica presente na planilha...'
python erasePolicy.py
echo 'feito'

#echo 'criando arquivos do MDP com base na planilha...'
#python spreadsheet2MDP.py $1
#echo 'feito'

echo 'resolvendo o MDP...'
../RL-QL.py $1
echo 'feito'

echo 'passando politica pra planilha...'
python policy2spreadsheet.py $1
echo 'feito'