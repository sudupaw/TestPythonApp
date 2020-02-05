pipeline {
    agent any
	stages
	{
		stage('SVN checkout on Jenkins')
		{
			steps
			{	
				checkout([$class: 'SubversionSCM', additionalCredentials: [], excludedCommitMessages: '', excludedRegions: '', excludedRevprop: '', excludedUsers: '', filterChangelog: false, ignoreDirPropChanges: false, includedRegions: '', locations: [[credentialsId: 'fc2c9edf-9bb5-4d6f-bed9-e9d19eddfe03', depthOption: 'infinity', ignoreExternalsOption: true, local: 'einvoice-app-falcon', remote: 'https://mobifly.xp-dev.com/svn/ewaybill/trunk/ETL/einvoice-app-falcon']], quietOperation: true, workspaceUpdater: [$class: 'UpdateUpdater']])
			}
		}		
		stage('Deployment')
		{
			steps
			{
				script
				{ 
					def version = "1.2" 
					ENVIRONMENT="${ENVIRONMENT}"
					echo ENVIRONMENT
					switch (ENVIRONMENT)
					{
						case "QA_EINVOICE":
						server="11.0.2.125"
						password="qwerty123"
						port="9191"
						pyth="python3.6"
						break
					}
					bat "echo y| plink -ssh ${server} -l root -pw ${password} rm -rf ${ENVIRONMENT}"
					bat "echo y| plink -ssh ${server} -l root -pw ${password} mkdir ${ENVIRONMENT}"
					bat "echo y| pscp -pw ${password} -r einvoice-app-falcon root@${server}:/root/${ENVIRONMENT}"
					bat "echo y| pscp -pw ${password} -r einvoice-app-falcon/script.sh root@${server}:/root/${ENVIRONMENT}"
					bat "echo y| plink -v -ssh ${server} -l root -pw ${password}  bash ${ENVIRONMENT}/script.sh ${ENVIRONMENT} ${server} ${port} ${pyth}"
				}
			}
			post
			{
				failure
				{
					emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
					recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
					subject: "Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
					to: "masum.mobifly@gmail.com,ewaybill@mobifly.in"
				}
			}
		}
	}
}
