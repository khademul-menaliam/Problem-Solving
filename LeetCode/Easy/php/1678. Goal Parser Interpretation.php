function interpret($command) {
        return str_replace("()", "o", $command);
       // return str_replace(['()', '(al)'], ['o', 'al'], $command);
       
        return str_replace("(al)", "al", $command);
    }