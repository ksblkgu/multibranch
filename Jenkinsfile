pipeline {
    agent any
    options {
        skipDefaultCheckout()
    }
    stages {
        stage("Checkout") {
            step {
                checkout(changelog: false, poll: false, scm: [
                    $class: 'GitSCM',
                    branches: [
                        [name: 'master'],
                    ],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [
                            $class: 'RelativeTargetDirectory',
                            relativeTargetDir: 'src',
                        ],
                    ],
                    submoduleCfg: [],
                    userRemoteConfigs: [
                        [
                            url: 'https://github.com/ksblkgu/multibranch'
                        ],
                    ],
                ])
            }
        }
    }
}