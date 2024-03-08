<?php
	$nome = $_POST['nome'];
	$idade = $_POST['idade'];
	if ($idade >= 0 and $idade < 13) {
		print $nome . ' é Criança';
	} else {
		if ($idade < 18) {
			print $nome . ' é um Adolescente';
		} else  {
			if ($idade < 60)
				print $nome . ' é Adulto(a)';
			else
				print $nome . ' é Idoso(a)';		
		}
	}
?>