import sys

def main():
    argvLength = len(sys.argv)
    name = sys.argv[argvLength-1]

    nameModel = '''
import lombok.*;

import javax.persistence.*;

@Builder(toBuilder = true)
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Setter
@Getter
@Entity
@Table(name = "")
public class ''' + name + '''Model {
    @Id
    @GeneratedValue
    @Column(name = "ID")
    private Long id;

}
'''

    f1 = open(name + "Model.java", "w")
    f1.write(nameModel)
    f1.close()

    # open and read the file after the appending:
    f1 = open(name + "Model.java", "r")
    print(f1.read())

    nameModelComparator = '''   
import java.util.Comparator;

public class ''' + name + '''ModelComparator implements Comparator<''' + name + '''Model> {
    @Override
    public int compare(''' + name + '''Model o1, ''' + name + '''Model o2) {
        return o1.getId().compareTo(o2.getId());
    }
}
'''

    f2 = open(name + "ModelComparator.java", "w")
    f2.write(nameModelComparator)
    f2.close()

    # open and read the file after the appending:
    f2 = open(name + "ModelComparator.java", "r")
    print(f2.read())

    nameRepository = '''
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface ''' + name + '''Repository extends JpaRepository<''' + name + '''Model, Long> {
}
'''

    f3 = open(name + "Repository.java", "w")
    f3.write(nameRepository)
    f3.close()

    # open and read the file after the appending:
    f3 = open(name + "Repository.java", "r")
    print(f3.read())

    nameService = '''
import lombok.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Builder(toBuilder = true)
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Setter
@Getter
@Service
public class ''' + name + '''Service {
    @Autowired
    private ''' + name + '''Repository ''' + name.lower() + '''Repository;

    public void save(''' + name + '''Model ''' + name.lower() + '''Model) {
        ''' + name.lower() + '''Repository.save(''' + name.lower() + '''Model);
    }

    public List<''' + name + '''Model> findAll() {
        return ''' + name.lower() + '''Repository.findAll();
    }
}
'''

    f4 = open(name + "Service.java", "w")
    f4.write(nameService)
    f4.close()

    # open and read the file after the appending:
    f4 = open(name + "Service.java", "r")
    print(f4.read())

# call with python3 CreatSpringPersistenceClasses.py name
main()