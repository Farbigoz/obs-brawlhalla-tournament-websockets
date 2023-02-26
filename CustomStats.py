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
    bh.postmatch.u.dHeavy.uses +
    bh.postmatch.u.recovery.uses +
    bh.postmatch.u.gp.uses
)

# Количество тяжёлых атак на первом оружии
bh.postmatch.w1.heavyUses = (
    bh.postmatch.w1.nHeavy.uses +
    bh.postmatch.w1.sHeavy.uses +
    bh.postmatch.w1.dHeavy.uses +
    bh.postmatch.w1.recovery.uses +
    bh.postmatch.w1.gp.uses
)

# Количество тяжёлых атак на втором оружии
bh.postmatch.w2.heavyUses = (
    bh.postmatch.w2.nHeavy.uses +
    bh.postmatch.w2.sHeavy.uses +
    bh.postmatch.w2.dHeavy.uses +
    bh.postmatch.w2.recovery.uses +
    bh.postmatch.w2.gp.uses
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
    bh.postmatch.u.dHeavy.enemyHits +
    bh.postmatch.u.recovery.enemyHits +
    bh.postmatch.u.gp.enemyHits
)

# Количество попаданий тяжёлыми атаками на первом оружии
bh.postmatch.w1.heavyHits = (
    bh.postmatch.w1.nHeavy.enemyHits +
    bh.postmatch.w1.sHeavy.enemyHits +
    bh.postmatch.w1.dHeavy.enemyHits +
    bh.postmatch.w1.recovery.enemyHits +
    bh.postmatch.w1.gp.enemyHits
)

# Количество попаданий тяжёлыми атаками на втором оружии
bh.postmatch.w2.heavyHits = (
    bh.postmatch.w2.nHeavy.enemyHits +
    bh.postmatch.w2.sHeavy.enemyHits +
    bh.postmatch.w2.dHeavy.enemyHits +
    bh.postmatch.w2.recovery.enemyHits +
    bh.postmatch.w2.gp.enemyHits
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
    bh.postmatch.u.dHeavy.enemyDamage +
    bh.postmatch.u.recovery.enemyDamage +
    bh.postmatch.u.gp.enemyDamage
)

# Урон тяжёлых атак на первом оружии
bh.postmatch.w1.heavyDamageDealt = (
    bh.postmatch.w1.nHeavy.enemyDamage +
    bh.postmatch.w1.sHeavy.enemyDamage +
    bh.postmatch.w1.dHeavy.enemyDamage +
    bh.postmatch.w1.recovery.enemyDamage +
    bh.postmatch.w1.gp.enemyDamage
)

# Урон тяжёлых атак на втором оружии
bh.postmatch.w2.heavyDamageDealt = (
    bh.postmatch.w2.nHeavy.enemyDamage +
    bh.postmatch.w2.sHeavy.enemyDamage +
    bh.postmatch.w2.dHeavy.enemyDamage +
    bh.postmatch.w2.recovery.enemyDamage +
    bh.postmatch.w2.gp.enemyDamage
)

# Цель - Урон всех тяжёлых атак
bh.postmatch.totalHeavyDamage = (
    bh.postmatch.u.heavyDamageDealt +
    bh.postmatch.w1.heavyDamageDealt +
    bh.postmatch.w2.heavyDamageDealt
)






# Количество лёгких атак без оружия
bh.postmatch.u.lightUses = (
    bh.postmatch.u.nLight.uses +
    bh.postmatch.u.sLight.uses +
    bh.postmatch.u.dLight.uses +
    bh.postmatch.u.nAir.uses +
    bh.postmatch.u.sAir.uses +
    bh.postmatch.u.dAir.uses
)

# Количество лёгких атак на первом оружии
bh.postmatch.w1.lightUses = (
    bh.postmatch.w1.nLight.uses +
    bh.postmatch.w1.sLight.uses +
    bh.postmatch.w1.dLight.uses +
    bh.postmatch.w1.nAir.uses +
    bh.postmatch.w1.sAir.uses +
    bh.postmatch.w1.dAir.uses
)

# Количество лёгких атак на втором оружии
bh.postmatch.w2.lightUses = (
    bh.postmatch.w2.nLight.uses +
    bh.postmatch.w2.sLight.uses +
    bh.postmatch.w2.dLight.uses +
    bh.postmatch.w2.nAir.uses +
    bh.postmatch.w2.sAir.uses +
    bh.postmatch.w2.dAir.uses
)

# Цель - Количество лёгких атак
bh.postmatch.totalLightUses = (
    bh.postmatch.u.lightUses +
    bh.postmatch.w1.lightUses +
    bh.postmatch.w2.lightUses
)


# Количество попаданий лёгкими атаками без оружия
bh.postmatch.u.lightHits = (
    bh.postmatch.u.nLight.enemyHits +
    bh.postmatch.u.sLight.enemyHits +
    bh.postmatch.u.dLight.enemyHits +
    bh.postmatch.u.nAir.enemyHits +
    bh.postmatch.u.sAir.enemyHits +
    bh.postmatch.u.dAir.enemyHits
)

# Количество попаданий лёгкими атаками на первом оружии
bh.postmatch.w1.lightHits = (
    bh.postmatch.w1.nLight.enemyHits +
    bh.postmatch.w1.sLight.enemyHits +
    bh.postmatch.w1.dLight.enemyHits +
    bh.postmatch.w1.nAir.enemyHits +
    bh.postmatch.w1.sAir.enemyHits +
    bh.postmatch.w1.dAir.enemyHits
)

# Количество попаданий лёгкими атаками на втором оружии
bh.postmatch.w2.lightHits = (
    bh.postmatch.w2.nLight.enemyHits +
    bh.postmatch.w2.sLight.enemyHits +
    bh.postmatch.w2.dLight.enemyHits +
    bh.postmatch.w2.nAir.enemyHits +
    bh.postmatch.w2.sAir.enemyHits +
    bh.postmatch.w2.dAir.enemyHits
)

# Цель - Количество попаданий лёгкими атаками
bh.postmatch.totalLightHits = (
    bh.postmatch.u.lightHits +
    bh.postmatch.w1.lightHits +
    bh.postmatch.w2.lightHits
)

# Цель - Аккуратность лёгких атак
# (Количество попаданий / Количество атак) = 0.xxx * 100 = xx.x + " %" = xx.x %
bh.postmatch.lightAccuracy = (
    (bh.postmatch.totalLightHits / bh.postmatch.totalLightUses) * 100 + " %"
)



# Урон лёгких атак без оружия
bh.postmatch.u.lightDamageDealt = (
    bh.postmatch.u.nLight.enemyDamage +
    bh.postmatch.u.sLight.enemyDamage +
    bh.postmatch.u.dLight.enemyDamage +
    bh.postmatch.u.nAir.enemyDamage +
    bh.postmatch.u.sAir.enemyDamage +
    bh.postmatch.u.dAir.enemyDamage
)

# Урон лёгких атак на первом оружии
bh.postmatch.w1.lightDamageDealt = (
    bh.postmatch.w1.nLight.enemyDamage +
    bh.postmatch.w1.sLight.enemyDamage +
    bh.postmatch.w1.dLight.enemyDamage +
    bh.postmatch.w1.nAir.enemyDamage +
    bh.postmatch.w1.sAir.enemyDamage +
    bh.postmatch.w1.dAir.enemyDamage
)

# Урон лёгких атак на втором оружии
bh.postmatch.w2.lightDamageDealt = (
    bh.postmatch.w2.nLight.enemyDamage +
    bh.postmatch.w2.sLight.enemyDamage +
    bh.postmatch.w2.dLight.enemyDamage +
    bh.postmatch.w2.nAir.enemyDamage +
    bh.postmatch.w2.sAir.enemyDamage +
    bh.postmatch.w2.dAir.enemyDamage
)

# Цель - Урон всех лёгких атак
bh.postmatch.totalLightDamage = (
    bh.postmatch.u.lightDamageDealt +
    bh.postmatch.w1.lightDamageDealt +
    bh.postmatch.w2.lightDamageDealt
)


