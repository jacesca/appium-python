def before_all(context):
    print('1.1 BEFORE ALL (each step/scenario/tag/feature)..................')


def after_all(context):
    print('1.2 AFTER ALL (each step/scenario/tag/feature)...................')


def before_tag(context, tag):
    print(f'2.1 BEFORE {tag} TAG............................................')


def after_tag(context, tag):
    print(f'2.2 AFTER {tag} TAG.............................................')


def before_feature(context, feature):
    print(f'3.1 BEFORE {feature} FEATURE....................................')


def after_feature(context, feature):
    print(f'3.2 AFTER {feature} FEATURE.....................................')


def before_scenario(context, scenario):
    print(f'4.1 BEFORE {scenario} SCENARIO..................................')


def after_scenario(context, scnario):
    print(f'4.2 AFTER {scnario} SCENARIO....................................')


def before_step(context, step):
    print(f'5.1 BEFORE {step} STEP..........................................')


def after_step(context, step):
    print(f'5.2 AFTER {step} STEP...........................................')
