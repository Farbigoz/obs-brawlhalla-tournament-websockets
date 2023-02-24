from StatsCommandsTree import bhTree as bh


# Цель - Сид с припиской "Сид: "
bh.prematch.mseed = (
    bh.empty + "Сид: " + bh.prematch.seed
)


# Цель - Урон без оружия
bh.postmatch.u.damageDealt = (
    bh.postmatch.u.throw.enemyDamage +
    bh.postmatch.u.recovery.enemyDamage +
    bh.postmatch.u.gp.enemyDamage +
    bh.postmatch.u.nLight.enemyDamage +
    bh.postmatch.u.sLight.enemyDamage +
    bh.postmatch.u.dLight.enemyDamage +
    bh.postmatch.u.nAir.enemyDamage +
    bh.postmatch.u.sAir.enemyDamage +
    bh.postmatch.u.dAir.enemyDamage +
    bh.postmatch.u.nHeavy.enemyDamage +
    bh.postmatch.u.sHeavy.enemyDamage +
    bh.postmatch.u.dHeavy.enemyDamage
)


# Цель - Количество атак без оружия
bh.postmatch.u.uses = (
    bh.postmatch.u.throw.uses +
    bh.postmatch.u.recovery.uses +
    bh.postmatch.u.gp.uses +
    bh.postmatch.u.nLight.uses +
    bh.postmatch.u.sLight.uses +
    bh.postmatch.u.dLight.uses +
    bh.postmatch.u.nAir.uses +
    bh.postmatch.u.sAir.uses +
    bh.postmatch.u.dAir.uses +
    bh.postmatch.u.nHeavy.uses +
    bh.postmatch.u.sHeavy.uses +
    bh.postmatch.u.dHeavy.uses
)


# Количество тяжёлых атак без оружия
bh.postmatch.u.heavyUses = (
    bh.postmatch.u.nHeavy.uses +
    bh.postmatch.u.sHeavy.uses +
    bh.postmatch.u.dHeavy.uses
)

# Количество тяжёлых атак на первом оружии
bh.postmatch.w1.heavyUses = (
    bh.postmatch.w1.nHeavy.uses +
    bh.postmatch.w1.sHeavy.uses +
    bh.postmatch.w1.dHeavy.uses
)

# Количество тяжёлых атак на втором оружии
bh.postmatch.w2.heavyUses = (
    bh.postmatch.w2.nHeavy.uses +
    bh.postmatch.w2.sHeavy.uses +
    bh.postmatch.w2.dHeavy.uses
)

# Цель - Количество тяжёлых атак
bh.postmatch.totalHeavyUses = (
    bh.postmatch.u.heavyUses +
    bh.postmatch.w1.heavyUses +
    bh.postmatch.w2.heavyUses
)


# Количество попаданий тяжёлыми атаками без оружия
bh.postmatch.u.heavyHits = (
    bh.postmatch.u.nHeavy.enemyHits +
    bh.postmatch.u.sHeavy.enemyHits +
    bh.postmatch.u.dHeavy.enemyHits
)

# Количество попаданий тяжёлыми атаками на первом оружии
bh.postmatch.w1.heavyHits = (
    bh.postmatch.w1.nHeavy.enemyHits +
    bh.postmatch.w1.sHeavy.enemyHits +
    bh.postmatch.w1.dHeavy.enemyHits
)

# Количество попаданий тяжёлыми атаками на втором оружии
bh.postmatch.w2.heavyHits = (
    bh.postmatch.w2.nHeavy.enemyHits +
    bh.postmatch.w2.sHeavy.enemyHits +
    bh.postmatch.w2.dHeavy.enemyHits
)

# Цель - Количество попаданий тяжёлыми атаками
bh.postmatch.totalHeavyHits = (
    bh.postmatch.u.heavyHits +
    bh.postmatch.w1.heavyHits +
    bh.postmatch.w2.heavyHits
)

# Цель - Аккуратность тяжёлых атак
# (Количество попаданий / Количество атак) = 0.xxx * 100 = xx.x + " %" = xx.x %
bh.postmatch.heavyAccuracy = (
    (bh.postmatch.totalHeavyHits / bh.postmatch.totalHeavyUses) * 100 + " %"
)



# Урон тяжёлых атак без оружия
bh.postmatch.u.heavyDamageDealt = (
    bh.postmatch.u.nHeavy.enemyDamage +
    bh.postmatch.u.sHeavy.enemyDamage +
    bh.postmatch.u.dHeavy.enemyDamage
)

# Урон тяжёлых атак на первом оружии
bh.postmatch.w1.heavyDamageDealt = (
    bh.postmatch.w1.nHeavy.enemyDamage +
    bh.postmatch.w1.sHeavy.enemyDamage +
    bh.postmatch.w1.dHeavy.enemyDamage
)

# Урон тяжёлых атак на втором оружии
bh.postmatch.w2.heavyDamageDealt = (
    bh.postmatch.w2.nHeavy.enemyDamage +
    bh.postmatch.w2.sHeavy.enemyDamage +
    bh.postmatch.w2.dHeavy.enemyDamage
)

# Цель - Урон всех тяжёлых атак
bh.postmatch.totalHeavyDamage = (
    bh.postmatch.u.heavyDamageDealt +
    bh.postmatch.w1.heavyDamageDealt +
    bh.postmatch.w2.heavyDamageDealt
)




