<?php
	$nome = $_POST['nome'];
	$peso = $_POST['peso'];

	$agua = $peso * 0.05;
	$carboidratos = $peso * 6;
	$proteina = $peso * 2.5;

	print $nome . ' precisa ingerir:<br>';
	print $agua . ' litros de água<br>';
	print $carboidratos . ' gramas de carbo<br>';
	print $proteina . ' gramas de proteinas';
?>