object Build : BuildType({

    name = "Build"

    triggers {
        vcs {
        }
    }

    steps {

        maven {
            goals = "clean install"
        }
    }

})
