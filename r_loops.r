help(c)

# for Schleifen:
# tue etwas mit i
# (wobei i in jedem Schleifendurchgang eine andere zahl annimmt)
# zahlen von 1 bis 10 (beides inclusive)
for (i in 1:10) {
  print(i)
}

for (i in 5:11) {
  print(i ** 2)
}

for (j in 2:10) {
  x <- j + 2
  print(x)
}

v1 <- c('a', 'aaa', 'b')

# i nimmt in jedem Schleifendurchlauf den nächsten Wert von v1 an
# startet beim ersten Element aus v1
for (i in v1) {
  print(i)
}

# seq() erstellt eine Sequenz
# seq(von, bis, by=schrittgröße)
for (i in seq(2, 10, by=2)) {
  print(i)
}


# while Schleifen:
# tue etwas solange eine bestimmte kondition zutrifft
x <- 5
while (x < 25){
  print(x)
  x <- x * 1.3
}
x
